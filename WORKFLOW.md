## Breakdown of ask

1. ~~Given Input return same list: strings & strings w/ nested props~~

2. ~~Given Input return same strings in GraphQL / JSON prettier format~~
3. Add Default view & Alphabetical return _Actually Ordering_ (modify list in place)
4. Extension -> Order by Ascending / Descending

## MVP Build/Proposals

1. ~~bash script mvp:~~
   ```echo string~~
   ~~~~Printf %s -> strings -> reformat as JSON~~~~
   In / Out reqs _FFast_
   ```
2. python application
   set value of `orignalString`
   func() -> transform string to JSON looing format ~~`json.dumps()`~~
   Remove !required chars
   throw into array
   func() -> `list.sort()`: reorder array items
   check for nested items and reorder
   return new list.
   send new string list to original transform fun()

## Iteration 1

1. User input of list w/ nested props
2. Default value remains given
   `originalString = userInput.getOrElse(given_string)`

## Iteration 2

- Arguments for A-Z vs Z-A order
