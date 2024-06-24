# How to configure AtCoder test

1. Generate Dropbox app.
2. Get the `APP_KEY` and `APP_SECRET` from Dropbox website.
3. Get access code.  
`https://www.dropbox.com/oauth2/authorize?client_id=${APP_KEY}&response_type=code&token_access_type=offline`
4. Get refresh token.
`curl https://api.dropbox.com/oauth2/token -u ${APP_KEY}:${APP_SECRET} -d grant_type=authorization_code -d code=${access_code}`
5. In the GitHub Action, get the access token and set it to env.
```
- name: Get dropbox token
    env:
        DROPBOX_REFRESH_TOKEN: ${{ secrets.DROPBOX_REFRESH_TOKEN }}
        DROPBOX_APP_KEY: ${{ secrets.DROPBOX_APP_KEY }}
        DROPBOX_APP_SECRET: ${{ secrets.DROPBOX_APP_SECRET }}
    run:  |
    {
        echo 'DROPBOX_TOKEN<<EOF'
        curl --silent https://api.dropbox.com/oauth2/token \
        -u ${DROPBOX_APP_KEY}:${DROPBOX_APP_SECRET} \
        -d grant_type=refresh_token \
        -d refresh_token=${DROPBOX_REFRESH_TOKEN} \
        | jq -r .access_token
        echo EOF
    } >> "$GITHUB_ENV"
```