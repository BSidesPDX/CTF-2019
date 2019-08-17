# RE100 - Magic Numbers - Solution

## Basic analysis

It's good to start with collecting basic information about the binary.  The `file` command on Linux is a good start.

```
$ file magicnumbers 
magicnumbers: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f69667c467d3e522a8684095219c9416eaa9874f, for GNU/Linux 3.2.0, not stripped
```

This is a 64-bit Linux binary.  Luckily, it's not stripped, so we still have legible function names.  You can also try running `strings` on the binary to see if the flag is hardcoded in plain-text.  Unfortunately, that isn't the case here.

## Running the binary

Let's try running the binary (it's good practice to only run unknown binaries in an isolated VM).

```
$ ./magicnumbers 
Welcome to Magic Numbers!
You will be prompted for 3 magic numbers.
After you enter each magic numbers, I will let you know if it's correct or not!
ProTip: Be sure you enter the numbers in decimal format (not hex!)
In other words, if the magic number is 0x539, you should enter 1337 into the program.
Enter Magic Number 1/3: 
```

Let's see what happens when we enter a random number.

```
$ ./magicnumbers 
Welcome to Magic Numbers!
You will be prompted for 3 magic numbers.
After you enter each magic numbers, I will let you know if it's correct or not!
ProTip: Be sure you enter the numbers in decimal format (not hex!)
In other words, if the magic number is 0x539, you should enter 1337 into the program.
Enter Magic Number 1/3: 10
Sorry, that is not the correct number.  You entered: 10
```

Looks like we need to figure out the correct magic number to proceed.

## Decompile with Ghidra

Let's use [Ghidra](https://ghidra-sre.org/) to decompile the binary and see if we can find the magic number.  If video tutorials are your thing, checkout: [YouTube: GHIDRA Tutorial — Learn How to Use Reverse Engineering Tool](https://www.youtube.com/watch?v=xDyLy0zLV7s).

### Load the binary into Ghidra

You can perform the following steps to load the project into Ghidra

1. Launch Ghidra.
2. Click `File -> New Project` or `Ctrl+N` to launch the new project wizard.
3. Select `Non-Shared Project` and click `Next >>`.
4. Choose a `Project Directory` and pick a name for your project.
5. Click `Finish`.
6. Using your filemanager, click and drag the challenge binary into the Ghidra window
7. The default options are usually good enough, click `Ok` on the pop-up.
8. You should now see the `Import Results Summary` window pop-up, click `Ok` on this as well.
9. Click and drag the binary in the Ghidra window to the icon of the green dragon (or `Right Click the binary -> Open With -> CodeBrowser`)
10. You should now see a pop-up for `Analysis Options`.  The defaults are usually good, press `Analyze`.
11. Wait for analysis to complete.


### Get the decompiled source for the `main()` function

When reversing, `main` is usually the first place you should start looking.

To pull up the disassembly and decompiled code for `main`, perofrm the following steps:

1. Find the `Symbol Tree` window on the left-hand side.
2. Expand the `Functions` folder
3. Scroll through the list, and click on `main`.
4. The middle window will show the diassembly for `main` and the right-hand window will show the decompiled source.

## Analyze the decompiled `main()` source

The decompiled source for main is below:

```c
undefined8 main(void)

{
  int iVar1;
  undefined8 uVar2;
  uchar *in;
  size_t inlen;
  long in_FS_OFFSET;
  uint local_44;
  uint local_40;
  uint local_3c;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  undefined2 local_14;
  undefined local_12;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts("Welcome to Magic Numbers!");
  puts("You will be prompted for 3 magic numbers.");
  puts("After you enter each magic numbers, I will let you know if it\'s correct or not!");
  puts("ProTip: Be sure you enter the numbers in decimal format (not hex!)");
  puts("In other words, if the magic number is 0x539, you should enter 1337 into the program.");
  printf("Enter Magic Number 1/3: ");
  iVar1 = __isoc99_scanf(&DAT_0010215f,&local_44);
  if (iVar1 == 1) {
    if (local_44 == 0x539) {
      puts("Ok, I gave you that one free, let\'s make it a little harder now");
      printf("Enter Magic Number 2/3: ");
      iVar1 = __isoc99_scanf(&DAT_0010215f,&local_40);
      if (iVar1 == 1) {
        if (local_40 == 0x7a69) {
          printf("Enter Magic Number 3/3: ");
          iVar1 = __isoc99_scanf(&DAT_0010215f,&local_3c);
          if (iVar1 == 1) {
            if (local_3c == 0x12b9b0a1) {
              puts("Good job!! -- 1 second while I decrypt your flag for you!");
              local_38 = 0x3d586c6d5d714c4a;
              local_30 = 0x63672c6b2a767460;
              local_28 = 0x5f676e3872675b38;
              local_20 = 0x613b6d675d766e38;
              local_18 = 0x603c6667;
              local_14 = 0x5c39;
              local_12 = 0x85;
              decrypt((EVP_PKEY_CTX *)&local_38,(uchar *)0x27,(size_t *)0x613b6d675d766e38,in,inlen)
              ;
              puts((char *)&local_38);
              uVar2 = 0;
            }
            else {
              printf("Sorry, that is not the correct number.  You entered: %d\n",(ulong)local_3c);
              uVar2 = 1;
            }
          }
          else {
            puts("Did you enter a number?");
            uVar2 = 1;
          }
        }
        else {
          printf("Sorry, that is not the correct number.  You entered: %d\n",(ulong)local_40);
          uVar2 = 1;
        }
      }
      else {
        puts("Did you enter a number?");
        uVar2 = 1;
      }
    }
    else {
      printf("Sorry, that is not the correct number.  You entered: %d\n",(ulong)local_44);
      uVar2 = 1;
    }
  }
  else {
    puts("Did you enter a number?");
    uVar2 = 1;
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}
```

The goal is to get to this part of the program to get the flag:
```c
              puts("Good job!! -- 1 second while I decrypt your flag for you!");
              local_38 = 0x3d586c6d5d714c4a;
              local_30 = 0x63672c6b2a767460;
              local_28 = 0x5f676e3872675b38;
              local_20 = 0x613b6d675d766e38;
              local_18 = 0x603c6667;
              local_14 = 0x5c39;
              local_12 = 0x85;
              decrypt((EVP_PKEY_CTX *)&local_38,(uchar *)0x27,(size_t *)0x613b6d675d766e38,in,inlen)
              ;
              puts((char *)&local_38);
              uVar2 = 0;
```

But to do so, the program needs to pass through a number of `if` statements.


The following is executed immediately upon launching the binary:

```c
puts("Welcome to Magic Numbers!");
puts("You will be prompted for 3 magic numbers.");
puts("After you enter each magic numbers, I will let you know if it\'s correct or not!");
puts("ProTip: Be sure you enter the numbers in decimal format (not hex!)");
puts("In other words, if the magic number is 0x539, you should enter 1337 into the program.");
printf("Enter Magic Number 1/3: ");
iVar1 = __isoc99_scanf(&DAT_0010215f,&local_44);
```

If you are not familiar with a specific Linux C function, you can use `man` to get more information.  For example, we can run `man scanf` to find the following information:

```
The scanf() function reads input from the standard input stream stdin
```

And it returns:

```
On success, these functions return the number of input items successfully matched and assigned
```

So let's look at the next few lines of code:

```c
iVar1 = __isoc99_scanf(&DAT_0010215f,&local_44);
if (iVar1 == 1) {
  if (local_44 == 0x539) {
```

So the program is ensuring that `1` was returned by `scanf` (meaning 1 input item was successfully matched and assigned).  Next, it checks that this input number is equal to `0x539`.

Wait, this number looks familiar!  Remember what the program printed earlier:

```
ProTip: Be sure you enter the numbers in decimal format (not hex!)
In other words, if the magic number is 0x539, you should enter 1337 into the program.
```

So let's make sure we have a way to convert 0x539.  I use `python` to convert the hext number to decimal, but there are lots of other ways to do it (Google, etc.).

```
$ python
Python 2.7.16 (default, Apr  6 2019, 01:42:57) 
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x539
1337
```

Let's test it out to make sure we progress through the program.

```
$ ./magicnumbers 
Welcome to Magic Numbers!
You will be prompted for 3 magic numbers.
After you enter each magic numbers, I will let you know if it's correct or not!
ProTip: Be sure you enter the numbers in decimal format (not hex!)
In other words, if the magic number is 0x539, you should enter 1337 into the program.
Enter Magic Number 1/3: 1337
Ok, I gave you that one free, let's make it a little harder now
Enter Magic Number 2/3: 
```

Now let's find the next 2 numbers.

The next call to `scanf` is the following:

```c
      printf("Enter Magic Number 2/3: ");
      iVar1 = __isoc99_scanf(&DAT_0010215f,&local_40);
      if (iVar1 == 1) {
        if (local_40 == 0x7a69) {
```

So let's convert `0x7a69` to decimal.

```
>>> 0x7a69
31337
```

So our next number is `31337`.

Let's go ahead and find the last number.

```c
          printf("Enter Magic Number 3/3: ");
          iVar1 = __isoc99_scanf(&DAT_0010215f,&local_3c);
          if (iVar1 == 1) {
            if (local_3c == 0x12b9b0a1) {
```

```
>>> 0x12b9b0a1
314159265
```


So the magic numbers are:
1. `1337`
2. `31337`
3. `314159265`

## Run the program with the magic numbers

```
$ ./magicnumbers 
Welcome to Magic Numbers!
You will be prompted for 3 magic numbers.
After you enter each magic numbers, I will let you know if it's correct or not!
ProTip: Be sure you enter the numbers in decimal format (not hex!)
In other words, if the magic number is 0x539, you should enter 1337 into the program.
Enter Magic Number 1/3: 1337
Ok, I gave you that one free, let's make it a little harder now
Enter Magic Number 2/3: 31337
Enter Magic Number 3/3: 314159265
Good job!! -- 1 second while I decrypt your flag for you!
BSidesPDX{n1c3_j0b_y0u_f0und_t3h_m4g1c}
```
