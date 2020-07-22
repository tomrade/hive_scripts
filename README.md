# hive_scripts
Tools and Connectors to work with thehive

# Alert Generators

These are thing used to make alerts. So far we have

## motioneye

A simple script to use with motioneye in order to create an alert when a camera detects movement. It us run from the motioneye console as follows (notice the variables from the motioneye console)

```
python3 hive_motioneye.py -c hive_motioneye.json -t %Y-%m-%d_%H-%M-%S -e %V -n "Camera Name"
```

Or from the shell as

``` bash
python3 hive_motioneye.py -c hive_motioneye.json -t 2020-07-21_09-27-39 -e 1337 -n "Camera Name"
```

The API details are stored in the JSON config file.