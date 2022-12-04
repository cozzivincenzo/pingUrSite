
# pingUrSite - A telegram pinger bot!

pingUrSite is usefulless bot to check the status of your own website and notify you when it goes offline


## Run Locally

To run the bot locally on your machine, follow this steps:

Clone the project

```bash
  git clone https://github.com/cozzivincenzo/pingUrSite.git
```

Go to the project directory

```bash
  cd pingUrSite
```

Set this environment variables in your .env file

`TOKEN = "XXXXX:XXXXXXXXX"`

`USERID = "XXXXXXXX"`

`URL = "http://linktoyourwebsite"`

Run the bot

```bash
  python app.py
```


## Environment Variables Reference


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `TOKEN` | `string` | **Required**. Your bot token |
| `USERID` | `int` | **Required**. Your telegram user ID |
| `URL` | `string` | **Required**. The URL of the web you want to ping  |



## Tech Stack

**Server:** Redis, Python 3.7.3


### Acknowledgements

 - [How to create a telegram bot](https://core.telegram.org/bots#how-do-i-create-a-bot)
 - [How to install Redis on Linux server](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)
 - [How to install Python 3.7 on Linux server](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)


## Support

For support, text me at [@Rcodi](https://t.me/rcodi)


## License

This project is under [MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions are always welcome!

Feel free to fork the project it to improve it and help it grow!

