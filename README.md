# snowflake2
Based on <a href="https://github.com/falcondai/python-snowflake/blob/69898a84ef2b9c4919b5940120f8fc8e90723e0f/snowflake.py">falcondai and fenhl's Python snowflake tool</a>, but with documentation and simliarities to Discord.

## Installation instructions
Installation is easy. Just read the docs below then run this command:
```
pip install snowflake2==0.1.1
```

## Docs
### `make_snowflake`

This is a function to generate a snowflake. 

This function does not return an integer snowflake - it returns a string.

Paramters are listed below.

Here's an example if you want to look at it after reading the below docs:
```python
make_snowflake(time.time(), 0, 0, 0)
```

#### `timestamp_ms`
This is an epoch time paramter. You can get one by running `time.time()`.

Basically, an oversimplified description of the way a snowflake works is by looking at a "twepoch", then subtracting a normal epoch from it (but there are other factors in it, as detailed in the rest of this documentation). That is why you need a `timestamp_ms`.

Note that the default twepoch is `1639853814` here, but Twitter's is `1288834974657`

Discord has <a href="https://discord.com/developers/docs/reference#snowflakes">some information</a> on this as well.
![image](https://user-images.githubusercontent.com/61570792/146653588-2142e8a1-ac07-45ea-b78c-a6dc6ed605bc.png)

#### `worker_id`
This can  be used internally to keep track of the worker for each snowflake, <a href="https://discordapp.com/developers/docs/reference">inspired by Discord's snowflake system</a>. 

#### `process_id`
This can be used internally to keep track of the process for each snowflake, <a href="https://discordapp.com/developers/docs/reference">inspired by Discord's snowflake system</a>.

Discord's documentation shown in `worker_id` also applies here.

#### `increment_id`
This can be used to keep track of 12-bit increments for every generated ID on the aforementioned process.

### `snowflakeToTime`

Converts a snowflake to a Python `datetime`.

Takes a snowflake ID argument only and converts it to a datetime.

Example:

```python
snowflakeToTime(make_snowflake(time.time(), 0, 0, 0))
```
