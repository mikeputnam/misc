if [[ $UPGRADETYPE = "rel" ]];
    then print "Release upgrade. Got it."
    export RELEASEPATH=/home/$UPGRADETYPE   # where you put the files
elif [[ $UPGRADETYPE = "snp" ]];
    then print "Snapshot upgrade. Got it." 
    export RELEASEPATH=/home/$UPGRADETYPE   # where you put the files
else
    print "Must run with: UPGRADETYPE=rel or snp ", $0
    exit 1
fi
echo "running MAKEDEV..."
cd /dev
./MAKEDEV all
echo "running sysmerge..."
sysmerge -s ${RELEASEPATH}/etc53.tgz -x ${RELEASEPATH}/xetc53.tgz
echo "cleaning up..."
rm /usr/bin/lint
rm /usr/libexec/lint[12]
rm -r /usr/libdata/lint
rm /usr/share/man/man1/lint.1
rm /etc/rc.d/btd
rm /usr/sbin/pkg
rm /sbin/raidctl
rm /usr/share/man/man4/raid.4
rm /usr/share/man/man8/raidctl.8
rm /usr/libexec/tftpd
rm -r /usr/lib/gcc-lib/*-unknown-openbsd5.1
echo "starting pkg_add -ui"
pkg_add -ui
