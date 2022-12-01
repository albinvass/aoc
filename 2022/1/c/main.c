#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct Elf {
    unsigned int number;
    unsigned int calories;
};

struct Elves {
    size_t size;
    struct Elf elves[];
};

int push_back(struct Elves **es, struct Elf elf) {
    size_t x = *es ? es[0]->size : 0;
    size_t y = x + 1;

    if ((x & y) == 0) {
        void *temp = realloc(
            *es,
            sizeof **es + (x + y) * sizeof es[0]->elves[0]
        );

        if(!temp) { return 1; }  // Unable to allocate memory
        *es = temp;
    }
    es[0]->elves[x] = elf;
    es[0]->size = y;
    return 0;
}

int compare_elfs(const void* a, const void* b) {
    struct Elf arg1 = *(const struct Elf*)a;
    struct Elf arg2 = *(const struct Elf*)b;

    if(arg1.calories < arg2.calories) return 1;
    if(arg1.calories > arg2.calories) return -1;
    return 0;
}

int main() {
    FILE *fp;
    fp = fopen("../input.txt", "r");
    if (fp == NULL) {
        perror("Unable to open file");
        exit(1);
    }
    struct Elves *elves = NULL;
    struct Elf elf = {0,0};
    char line[256];
    while(fgets(line, sizeof(line), fp)) {
        line[strcspn(line, "\r\n")] = 0;
        if (strlen(line) != 0) {
            unsigned int calories = strtol(line, NULL, 10);
            elf.calories += calories;
        } else {
            push_back(&elves, elf);
            elf.number = elf.number+1;
            elf.calories = 0;
        }
    }

    qsort(elves->elves, elves->size, sizeof(struct Elf), compare_elfs);
    printf("Top three elves:\n");
    int calorie_sum = 0;
    for(size_t i = 0; i<3; i++) {
        calorie_sum += elves->elves[i].calories;
        printf("    Elf #%d has %d calories\n", elves->elves[i].number, elves->elves[i].calories);
    }
    printf("Together they are carrying %d calories\n", calorie_sum);


    fclose(fp);
    free(elves);  // Dobby wants to be free
    exit(0);
}
