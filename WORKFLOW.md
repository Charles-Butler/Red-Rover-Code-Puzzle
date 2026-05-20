## Breakdown of ask

~~1. Given Input return same list: strings & strings w/ nested props~~

2. Given Input return same strings in GraphQL / JSON prettier format
3. Add Default view & Alphabetical return _Actually Ordering_ (modify list in place)
4. Extension -> Order by Ascending / Descending
5. Extension -> Given ANY custom input "..."

## MVP Build/Proposals

1. bash script mvp:
   Printf %s -> strings -> reformat as JSON
   In / Out reqs
2. python application
   func() -> transform string to JSON format
   func() -> list.sort()
   return new list.

## Iteration 1

1. User input of list w/ nested props
2. Default value remains given
   `originalString = userInput.getOrElse(given_string)`

## Iteration 2
