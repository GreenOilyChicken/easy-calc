def main(triplets):
    all_digits = set(range(10))
    five_comp_count = {}
    four_comp_count = {}
    
    n = len(triplets)
    # 检查所有三元组对
    for i in range(n):
        for j in range(i + 1, n):
            a = set(triplets[i])
            b = set(triplets[j])
            intersection = a & b
            # 共享一个数字的情况
            if len(intersection) == 1:
                union = a | b
                if len(union) == 5:
                    comp = tuple(sorted(all_digits - union))
                    five_comp_count[comp] = five_comp_count.get(comp, 0) + 1
            # 没有共享数字的情况
            elif len(intersection) == 0:
                union = a | b
                if len(union) == 6:
                    comp = tuple(sorted(all_digits - union))
                    four_comp_count[comp] = four_comp_count.get(comp, 0) + 1
    
    # 输出结果
    print("五元补集结果（来自共享1个数字的三元组对）")
    for comp, count in sorted(five_comp_count.items()):
        print(f"{list(comp)} : {count} 次")
    
    print("\n四元补集结果（来自无交集的三元组对）")
    for comp, count in sorted(four_comp_count.items()):
        print(f"{list(comp)} : {count} 次")

if __name__ == "__main__":
    example_triplets = [
        [2,6,8], [6,7,8], [2,6,9], [5,6,8], [6,8,9], [5,8,9], [0,2,8], [0,4,8], [4,7,9], [2,7,9]
    ]
    main(example_triplets)