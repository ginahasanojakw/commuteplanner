# === Stage 37: Add recommendations for the next useful action ===
# Project: CommutePlanner
def get_recommendations(self):
        """Suggest improvements based on usage patterns."""
        if not self.history:
            return ["Start tracking your commute to see insights."]
        
        total_time = sum(entry.duration for entry in self.history)
        most_common_route = max(set(entry.route for entry in self.history), key=list(self.history).count)
        
        recommendations = []
        
        if total_time > 0:
            avg_duration = total_time / len(self.history)
            if avg_duration > 60:
                recommendations.append(f"Your average commute is {avg_duration:.0f} minutes. Consider alternative routes or leaving earlier.")
            if self.history[0].route == self.history[-1].route:
                recommendations.append("You've been taking the same route recently. Try exploring alternatives.")
        
        if self.history[0].departure_time != self.history[-1].departure_time:
            recommendations.append("Your departure times vary. Try sticking to one time for consistency.")
        
        if self.history[0].cost != self.history[-1].cost:
            recommendations.append("Your costs vary. Track spending to find cheaper options.")
        
        if recommendations:
            return recommendations
        return ["You're doing great! Keep tracking your commute."]
