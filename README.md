# omu-linux-basics

Challenges for the [Linux Basics](https://omu.rce.so/lessons/linux-basics/) module of [**omu**](https://omu.rce.so/).

## Getting Started

### 0. Install `docker-compose`

Follow the instructions provided [here](https://docs.docker.com/compose/install/).

### 1. Clone this repository

```bash
git clone https://github.com/chickenRCE/omu-linux-basics.git
```

### 2. Start the challenges

```bash
cd omu-linux-basics
docker-compose up -d
```

It may take some time after you run `docker-compose up -d`, make sure you are in the `omu-linux-basics` directory when you run the command.

You should see similar output to this at the **end**

```
$ docker-compose up -d
...
Creating network "linux-basics_default" with the default driver
Creating linux-basics_cat_flag_1         ... done
Creating linux-basics_dog_flag_1         ... done
Creating linux-basics_bento_1            ... done
Creating linux-basics_peekaboo_column_1  ... done
Creating linux-basics_no_touch_no_see_1  ... done
Creating linux-basics_touch_no_see_1     ... done
Creating linux-basics_peekaboo_line_1    ... done
Creating linux-basics_catch_the_thiefs_1 ... done
```

### 3. Connect to bento

#### Linux/macOS
```bash
./connect
```

> Note: If you encounter an error, make sure to make the script executable
```bash
chmod +x ./connect
./connect
```

#### Windows
```
./connect.ps1
```

You should now be connected in the `bento` box, you can follow the instructions in the challenge pages to connect to each challenge.

```
$ ./connect
root@153ee55c9ccf:/# 
```

### 4. Finish

When you're done with the challenges for the day.
Bring down the challenges with the following command, you can always bring them back up later by following from steps **#2** onwards.

```
docker-compose down
```

> Note: Make sure you are in the `omu-linux-basics` directory when running this command.