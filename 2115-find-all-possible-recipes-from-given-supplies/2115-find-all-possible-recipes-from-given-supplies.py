from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:        
        graph = defaultdict(list)
        indegree = {r: 0 for r in recipes}

        for recipe, ings_list in zip(recipes, ingredients):
            indegree[recipe] = len(ings_list)
            for ing in ings_list:
                graph[ing].append(recipe)

        q = deque(supplies)
        result = []

        while q:
            ing = q.popleft()
            if ing in indegree:
                result.append(ing)

            for recipe in graph[ing]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)

        return result
