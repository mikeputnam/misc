#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/event.h>
#include <sys/time.h>
#include <errno.h>
#include <string.h>
#include <inttypes.h>
 
#define NUM_EVENT_SLOTS 1
#define NUM_EVENT_FDS 1
 
int main(int argc, char *argv[])
{
    char *path = argv[1];
    int kq;
    int event_fd;
    struct kevent events_to_monitor[NUM_EVENT_FDS];
    struct kevent event_data[NUM_EVENT_SLOTS];
    void *user_data;
    struct timespec timeout;
    unsigned int vnode_events;
 
    if (argc != 2) {
        fprintf(stderr, "Usage: monitor <file_path>\n");
        exit(-1);
    }
 
    if ((kq = kqueue()) < 0) {
        fprintf(stderr, "Could not open kernel queue.  Error was %s.\n", strerror(errno));
    }
 
    event_fd = open(path, O_RDONLY);
    if (event_fd <=0) {
        fprintf(stderr, "The file %s could not be opened for monitoring.  Error was %s.\n", path, strerror(errno));
        exit(-1);
    }
 
    user_data = path;
 
    /* Set the timeout to wake us every half second. */
    timeout.tv_sec = 0;        // 0 seconds
    timeout.tv_nsec = 500000000;    // 500 milliseconds
 
    /* Set up a list of events to monitor. */
    vnode_events = NOTE_RENAME;
    EV_SET( &events_to_monitor[0], event_fd, EVFILT_VNODE, EV_ADD | EV_CLEAR, vnode_events, 0, user_data);
 
    /* Handle events. */
    int num_files = 1;
    int continue_loop = 40; /* Monitor for twenty seconds. */
    while (--continue_loop) {
        int event_count = kevent(kq, events_to_monitor, NUM_EVENT_SLOTS, event_data, num_files, &timeout);
        if ((event_count < 0) || (event_data[0].flags == EV_ERROR)) {
            /* An error occurred. */
            fprintf(stderr, "An error occurred (event count %d).  The error was %s.\n", event_count, strerror(errno));
            break;
        }
        if (event_count) {
            printf("file renamed\n");
        }
        /* Reset the timeout.  In case of a signal interrruption, the
           values may change. */
        timeout.tv_sec = 0;        // 0 seconds
        timeout.tv_nsec = 500000000;    // 500 milliseconds
    }
    close(event_fd);
    return 0;
}

