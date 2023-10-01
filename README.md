# Hello world Python action

This action prints "Hello World" or "Hello" + the name of a person to greet to the log. This action is built with [`actions-python/toolkit`](https://github.com/actions-python/toolkit).

## Inputs

### `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

## Outputs

### `time`

The time we greeted you.

## Example usage

```yaml
uses: actions-python/hello-world-python-action@main
with:
  who-to-greet: 'Mona the Octocat'
```
