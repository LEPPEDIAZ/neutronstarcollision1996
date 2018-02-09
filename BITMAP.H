//BitMap Structure 

struct A{
	char type[2];                 /* Magic identifier            */
	unsigned long size;                       /* File size in bytes          */
	unsigned short int reserved1, reserved2;
	unsigned long offset;                     /* Offset to image data, bytes */
};

extern A HEADER,HEADER1;

struct B{
	unsigned long size;               /* Header size in bytes      */
	unsigned long width,height;                /* Width and height of image */
	unsigned short int planes;       /* Number of colour planes   */
	unsigned short int bits;         /* Bits per pixel            */
	unsigned long compression;        /* Compression type          */
	unsigned long imagesize;          /* Image size in bytes       */
	unsigned long xresolution,yresolution;     /* Pixels per meter          */
	unsigned long ncolours;           /* Number of colours         */
	unsigned long importantcolours;   /* Important colours         */
};
extern B INFOHEADER,INFOHEADER1;