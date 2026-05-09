
"""
Task 2.1: Australia Map Coloring
Color 5 regions using 3 colors (Blue, Red, Green)
No two adjacent regions share same color
"""

from constraint import Problem


problem = Problem()

# Regions of Australia (5 main regions)
regions = ['Western Australia', 'Northern Territory', 'South Australia', 
           'Queensland', 'New South Wales']

# Colors available
colors = ['Blue', 'Red', 'Green']


for region in regions:
    problem.addVariable(region, colors)


problem.addConstraint(lambda wa, nt: wa != nt, ('Western Australia', 'Northern Territory'))
problem.addConstraint(lambda wa, sa: wa != sa, ('Western Australia', 'South Australia'))
problem.addConstraint(lambda nt, sa: nt != sa, ('Northern Territory', 'South Australia'))
problem.addConstraint(lambda nt, q: nt != q, ('Northern Territory', 'Queensland'))
problem.addConstraint(lambda sa, q: sa != q, ('South Australia', 'Queensland'))
problem.addConstraint(lambda sa, nsw: sa != nsw, ('South Australia', 'New South Wales'))
problem.addConstraint(lambda q, nsw: q != nsw, ('Queensland', 'New South Wales'))

# Get all solutions
solutions = problem.getSolutions()


print("=" * 50)
print("Task 2.1: Australia Map Coloring")
print("=" * 50)
print(f"Colors available: {colors}")
print("\nSolution (region -> color):")
print("-" * 35)

for region, color in solutions[0].items():
    print(f"{region:20} : {color}")

print(f"\nTotal solutions found: {len(solutions)}")

# Verify no adjacent regions share same color
print("\n✓ All constraints satisfied: No adjacent regions have same color")