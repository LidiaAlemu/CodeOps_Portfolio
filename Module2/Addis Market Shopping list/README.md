# Addis Market Shopping List

A simple shopping list built with the state render loop.

## How it works

- Items are kept in an array called `items`.
- `render()` clears the list and rebuilds it from the array.
- The form adds an item, then calls `render()`.
- The list uses one click listener for the whole list (event delegation).
- Clicking a row toggles the bought state.
- Clicking the × button removes the item.
- The counter shows how many items are still left to buy