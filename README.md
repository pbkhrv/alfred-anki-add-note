# alfred-anki-add-note
Add notes to Anki from Alfred via an HTTP call (requires an Anki add-on)

# Status

Dirty hack, but works for me.

# Installation

This workflow does one thing and one thing only: it adds a new "basic" note to an Anki deck called "programming16".

When you call it up, it prompts you for the text to put on the front and the back of a note and then calls the [HTTP server that's running inside of your instance of Anki app via an add-on](https://github.com/pbkhrv/anki-http-server).

But you don't have a deck called "programming16", do you? I hear you. It's hardcoded for now, but you can easily change that - just install the workflow, double-click on the script and change the name of the deck. I don't really have the time right now to make it all configurable and nice...

## Important!

Did I mention that you need to also [install this Anki add-on](https://github.com/pbkhrv/anki-http-server)?
