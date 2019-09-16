<template>
  <div class="customers">
    <h3>Customers</h3>
    <Flag />
    <Customers />
  </div>
</template>

<script>
import Customers from '../components/Customers.vue';
import Flag from '../components/Flag.vue';

export default {
  name: 'login',
  components: {
    Customers,
    Flag,
  },
};
</script>

<style scoped>
/*
Project manager just sent me new designs
I can’t lie, InVision links are looking fly
Sales cannot wait, marketing wants a release date
Even the CEO wants to know how long it’ll take
How much are we going to push aside for that?
‘Cause I got backend tickets, I ain’t got no time for that
Too bad my PM told me this came from the top
So now I’m Googling “how to use flexbox”
Time to look, I open up the assets
I’ve been here for months, haven’t had to style yet
I wonder what’s in main.css?
Gotta catch my breath, dang it’s a crazy mess
I see a file called “overrides”, it’s just for IE6
A couple files for pages I’m pretty sure don’t exist
The markup makes it clear we don’t know how to use a grid
Cause every other line is line break or clearfix

(Chorus 2x)
Mess.css
It’s a mess.css
And I forgot mobile and tablet
Change my resume from full-stack to just backend

My divs got children and the children have so many kids
There’s like 50 indentation layers to this s***
We got a class for floating right, 3 for floating left
One named .size-12 that’s actually 10px text
One named .text-dark but it’s color: fff
One named .light-green, it also has the wrong hex
Inspect element, I’m taking guesses in the browser
I gotta center this vertically? Give me 7 hours
Plus the app relies on Bootstrap being imported
So I’m overriding, every rule is !important
It’s so annoying so I hit up my PM on Slack
Like “how exact should the app and the designs match?”
Move that, hide that, fade that
Yeah it sounds so simple when you say that
But the code’s so s***ty
We never cared as long as the app looked pretty

(Chorus 2x)
Mess.css
It’s a mess.css
And I forgot mobile and tablet
Change my resume from full-stack to just backend
*/
</style>
