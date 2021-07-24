# is-xxx-down

Is xxx down? Watch a website's status.

## Examples

- [Is Google down?](https://google.isdown.akise.app/)
- [Is GitHub down?](https://github.isdown.akise.app/)
- [Is VCB-S down?](https://vcb-s.isdown.akise.app/)

## Usage

The default server port is 8081, you can change it through `gunicorn.conf.py` or docker command line.

### 1. Linux Backend

```bash
export TITLE=xxx
export URL=https://xxx.com
gunicorn app:app -c gunicorn.conf.py
```

### 2. Docker Backend

```bash
docker run --name is_vcb-s_down -p 127.0.0.1:8081:8081 -e TITLE=VCB-S -e URL=https://vcb-s.com -d akise/is-xxx-down
```

## License

[MIT](LICENSE)
