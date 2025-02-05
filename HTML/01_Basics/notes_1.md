## Emmet 
- Use for fast paced coding.

## VSCODE Hack
- To duplicate a line use Alt + Shift + down arrow key
- For having multiple cursors click Alt + CLick

### Points
- Live server extension is used for auto refreshing the webpage made, whenever changes takes place.(Extension in VSCode)
- After click inspect, we wil be able to see a code as "Code Injected By Live-Server" -- This is used for telling the page that memeory has been updated please refresh.
- No need of manual refresh.
- Extension - Live Server Preview -- It helps see the web page on VScode
- To open live server in preview use Ctrl + Shift + P --search live server preview.
 
### Drawbacks of Live Server Preview
- No option of inspect
- No option of selecting an element

## About Heading h1
- Largest font of heading but not necessarily, we can change the size using CSS.
- It signifies the most important parts of the page.

## Tags
- <address> The Address Tag let's the page know that we are entering the address and formats it in the same way.

## Boilerplate Code
- A section of code which can be reused.
- !DOCTYPE html - lets the browser know it's an HTML Document.
- html lang="en" - As html is now a worldwide language, we need to specify the language as well in which we want to write the code.
- The Html code consistes of two children head & body.
- Head can have more children -- title.
- Body can have more children -- h1, h2,..
- head is the grandchild of html.
- Whatever is visible on the webpage is the part of body tag.
- From the head tag only two things are visible -- title and favicon (the icon present near the title of webpage)

- meta charset - is used for informing the browser about the character set we want to use
- To support smiley we can use charset = "UTF-16"
- Whichever tag you are opening should be closed.

## Keywords/Elements
- whatever is there inside h1 tag is all element including opening and closing of h1 tag.
- You can even use self closing br /.
- Nesting of tags can be done inside a tag as well using <span>.
- a anchor tag is used to add links.
- Goto MDn Docs for more details.

## Paragraph
- To write a random paragraph write p>loremCOUNT, replace count with the mnumber of words you need in the para.(Emmet is Used)
- br/ used for going to new line.
- hr - used to draw an horizontal line 

## Pre Tag
- Displays the data in same way as entered in the corresponding file.

## Heading Tag
- By default this text is bold

## Commenting
- Ctrl + / 

## Text Formatting
- For bold -- b in <> -- opening and closing required </>
- strong in <> alos does same, this is preferred more.
- For italics - i in <>
- em in <> is preferred
- For adding multiple bullet points usin Emmet Shortcut ul>li*Count, replace count with the numbrt of points.

- sup - for superscrippting
- sub - for subscripting
- del - for strikethrough
- mark - for highlighting
- Inline styling style = ""
- For clarity in styling tag write each style in new line

## Colors 
- rgba(14, 63, 225, 0.7); adding a corresponds to opaque(intensity)
- Adding style also depensa on which you are adding first, if css file is added last that is given priority

## Quote
- blockquote can be used, also an attribute cite(from where we have taken the value) can be added.
- q in <> is used for adding quotes
- abbr in <> used for adding abbreviations, add attribute title which will be seen while hovering.
- bdo tag is used for reading text from right to left if specified in attribute dir = "rtl" -- right to left

## Link Tag
- attribute target in anchor tag, if it is kept _blank, the href link is opened in a new browser.

## Image Tag
- To add an image saved in local, use ./ if file is in same folder, use ../ to move to another folder.

- Name of image in local should not have spaces in between

## Picture Tag
- It is used to define images for different sizes of screen where the image is to be loaded.

## Map Image
- gives us the ability to make the image area clickable.
- We can perform different functionality while clicking in images part
- We can display text while target area is clicked.
- 
