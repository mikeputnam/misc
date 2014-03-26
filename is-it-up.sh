function if_error
{
    if [[ $? -ne 0 ]]; then # check return code passed to function
        echo '' | mail -s "$1" nobody@example.com > /dev/null
    fi
}
#curl --silent --ssl --head http://dhmn.net/ | grep " 200 OK" > /dev/null
curl --silent --head http://dhmn.net/ | grep " 200 OK" > /dev/null
if_error "http://dhmn.net DOWN"

