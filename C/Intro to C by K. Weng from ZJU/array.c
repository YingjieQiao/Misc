#include <stdio.h>
#include <stdlib.h>

typedef struct{
  int *array;
  int size;
} Array;

Array array_create(int init_size);
void array_free(Array *a);
int array_size(const Array *a);
void array_inflate(Array *a, int more_size);

Array array_create(int init_size)
{
  Array a;
  a.size = init_size;
  a.array = (int*)malloc(sizeof(int)*a.size);
  return a;
}

void array_free(Array *a)
{
  free(a->array);
  a->array = NULL;
  a->size = 0;
}

//分装 protects the value inside a function. safer
int array_size(const Array *a)
{
  return (a->size);
}

int* array_at(Array *a, int more_size);
{
  if ( index >= a->size)
  {
    array_inflate(a, (index/BLOCK_SIZE+1)*BLOCK_SIZE-a->size)
  }
  return &(a->array[index]);
}

int array_get(const Array *a, int index)
{
  return a->array[index];
}

void array_set(Array *a, int index, int value)
{
  a->array[index] = value;


void array_inflate(Array *a, init more_size)
{
  int *p = (int*)malloc(sizeof(int)(a->size + more_size));
  int i;
  for (i = 0; i<a->size; i++)
  {
    p[i] = a->array[i];
  }
  free(a->array);
  a->array = p;
  a->size += more_size;
}
int main(int argc, char const *argv[]) {
  Array a = array_create(100);
  printf("%d\n", array(size(&a)));
  *array_at(&a,0) = 10;
  printf("%d\n", *array_at(&a,0));

  int number;
  int cnt = 0;
  while(number != -1))
  {
    //scanf("%d", &number);
    //*array_at(&a, cnt++) = number;
    scanf("%d", &number);
    if (number != -1)
    {
      *array_at(&a,cnt++) = number;
    }
  }
  array_free(&a);

  return 0;
}
