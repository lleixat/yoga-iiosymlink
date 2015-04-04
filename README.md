## Motivation

Personal usage. My sensors drivers are not complete (Yoga 2 Pro on Linux 3.19.2) so I need to access each device info via fixed path.

## Installation

```sh
> git clone https://github.com/lleixat/yoga-iiosymlink ~/trunk/yoga-iiosymlink
```

```sh
> cd  ~/trunk/yoga-iiosymlink
> ./install.sh
```

## Usage

In CLI or at session start:
```sh
> iiosymlink
```

Produce something like this:

```sh
Symlink: /sys/bus/iio/devices/iio:device0 -> /tmp/bus/iio/devices/gyro_3d
Symlink: /sys/bus/iio/devices/iio:device1 -> /tmp/bus/iio/devices/dev_rotation
Symlink: /sys/bus/iio/devices/iio:device2 -> /tmp/bus/iio/devices/magn_3d
Symlink: /sys/bus/iio/devices/iio:device3 -> /tmp/bus/iio/devices/accel_3d
Symlink: /sys/bus/iio/devices/iio:device4 -> /tmp/bus/iio/devices/incli_3d
Symlink: /sys/bus/iio/devices/iio:device5 -> /tmp/bus/iio/devices/als
```

Allow access to devices information. ie:

```sh
> ls /tmp/bus/iio/devices/als/
./       dev                      in_intensity_offset              name            subsystem@
../      in_intensity_both_raw    in_intensity_sampling_frequency  power/          trigger/
buffer/  in_intensity_hysteresis  in_intensity_scale               scan_elements/  uevent
```

## Licence

[DBAD](http://www.dbad-license.org/) PUBLIC LICENSE. More info: [http://www.dbad-license.org/](http://www.dbad-license.org/).
