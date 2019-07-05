

static const int MAX_BUF_SIZE = 16;
typedef struct
{
    int i;
    int j;
} MsgHeader;

typedef struct
{
    int flag;
    char buf[MAX_BUF_SIZE];
} MsgBody;

//void convert(int thousands, int hundreds, int tens, int ones);
