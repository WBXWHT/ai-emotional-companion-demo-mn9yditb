import json
import datetime
import random
from typing import Dict, List, Any

class EmotionalCompanion:
    """AI情感陪伴模拟类"""
    
    def __init__(self):
        # 模拟用户情绪数据库
        self.user_moods = {}
        # 话题库
        self.topics = [
            "今天工作中最有成就感的一件事是什么？",
            "最近有没有让你感到温暖的小瞬间？",
            "如果给自己放一天假，你最想做什么？",
            "最近有没有什么想学习的新技能？",
            "分享一个最近让你开心的小事吧"
        ]
    
    def record_daily_mood(self, user_id: str, mood: str, note: str = "") -> Dict[str, Any]:
        """记录每日情绪日记"""
        today = datetime.date.today().isoformat()
        
        if user_id not in self.user_moods:
            self.user_moods[user_id] = []
        
        entry = {
            "date": today,
            "mood": mood,
            "note": note,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        self.user_moods[user_id].append(entry)
        
        # 模拟AI生成回应
        ai_response = self._generate_ai_response(mood, note)
        
        return {
            "status": "success",
            "message": "情绪日记已记录",
            "data": entry,
            "ai_response": ai_response
        }
    
    def get_topic_recommendation(self, user_id: str) -> Dict[str, Any]:
        """获取智能话题推荐"""
        # 模拟基于用户历史情绪的简单推荐逻辑
        user_history = self.user_moods.get(user_id, [])
        
        if user_history:
            # 分析最近情绪倾向
            recent_moods = [entry["mood"] for entry in user_history[-3:]]
            mood_counts = {}
            for mood in recent_moods:
                mood_counts[mood] = mood_counts.get(mood, 0) + 1
            
            # 根据情绪选择话题
            if any(mood in ["难过", "沮丧", "焦虑"] for mood in recent_moods):
                topic = "有什么事情让你感到有压力吗？愿意和我聊聊吗？"
            elif any(mood in ["开心", "兴奋", "满足"] for mood in recent_moods):
                topic = "看到你最近状态不错，有什么秘诀可以分享吗？"
            else:
                topic = random.choice(self.topics)
        else:
            topic = random.choice(self.topics)
        
        return {
            "status": "success",
            "recommended_topic": topic,
            "timestamp": datetime.datetime.now().isoformat()
        }
    
    def get_mood_analysis(self, user_id: str) -> Dict[str, Any]:
        """获取情绪分析报告"""
        user_history = self.user_moods.get(user_id, [])
        
        if not user_history:
            return {
                "status": "error",
                "message": "暂无情绪记录"
            }
        
        # 简单情绪统计
        mood_stats = {}
        for entry in user_history:
            mood = entry["mood"]
            mood_stats[mood] = mood_stats.get(mood, 0) + 1
        
        # 模拟AI分析
        total_entries = len(user_history)
        if total_entries >= 3:
            recent_trend = "情绪波动正常" if len(set([e["mood"] for e in user_history[-3:]])) > 1 else "情绪稳定"
        else:
            recent_trend = "数据不足"
        
        return {
            "status": "success",
            "total_entries": total_entries,
            "mood_statistics": mood_stats,
            "recent_trend": recent_trend,
            "analysis_date": datetime.date.today().isoformat()
        }
    
    def _generate_ai_response(self, mood: str, note: str) -> str:
        """模拟AI生成个性化回应"""
        responses = {
            "开心": [
                "真为你感到高兴！继续保持这份好心情~",
                "开心的时刻值得被记住，感谢你与我分享这份喜悦！"
            ],
            "难过": [
                "我在这里陪着你，难过的时候说出来会好受一些",
                "感谢你信任我，愿意分享这些感受。一切都会慢慢好起来的"
            ],
            "平静": [
                "平静的时刻也很珍贵，享受当下的安宁吧",
                "在平静中积蓄力量，为更好的明天做准备"
            ],
            "焦虑": [
                "我理解你的不安，试着把大问题分解成小步骤",
                "焦虑是正常的情绪，让我们一起面对它"
            ]
        }
        
        # 根据情绪选择回应
        if mood in responses:
            base_response = random.choice(responses[mood])
        else:
            base_response = "感谢你记录此刻的心情，我在这里陪伴着你"
        
        # 如果用户写了备注，加入个性化内容
        if note:
            return f"{base_response} 你提到的'{note[:20]}...'让我更理解你的感受。"
        
        return base_response


def main():
    """主函数：演示AI情感陪伴核心功能"""
    print("=" * 50)
    print("AI情感陪伴演示系统")
    print("=" * 50)
    
    # 初始化情感陪伴系统
    companion = EmotionalCompanion()
    
    # 模拟用户ID
    user_id = "user_001"
    
    # 演示1：记录情绪日记
    print("\n1. 记录今日情绪日记")
    print("-" * 30)
    
    moods = ["开心", "难过", "平静", "焦虑", "兴奋"]
    selected_mood = random.choice(moods)
    note = "今天完成了重要的项目，虽然累但很有成就感"
    
    result = companion.record_daily_mood(user_id, selected_mood, note)
    print(f"记录情绪: {selected_mood}")
    print(f"日记内容: {note}")
    print(f"AI回应: {result['ai_response']}")
    
    # 演示2：获取话题推荐
    print("\n2. 智能话题推荐")
    print("-" * 30)
    
    topic_result = companion.get_topic_recommendation(user_id)
    print(f"推荐话题: {topic_result['recommended_topic']}")
    
    # 演示3：获取情绪分析
    print("\n3. 情绪分析报告")
    print("-" * 30)
    
    # 再添加几条模拟记录
    for _ in range(2):
        mood = random.choice(moods)
        companion.record_daily_mood(user_id, mood, f"模拟记录{mood}情绪")
    
    analysis = companion.get_mood_analysis(user_id)
    if analysis["status"] == "success":
        print(f"总记录数: {analysis['total_entries']}")
        print(f"情绪统计: {json.dumps(analysis['mood_statistics'], ensure_ascii=False)}")
        print(f"近期趋势: {analysis['recent_trend']}")
    
    # 演示4：模拟多日使用
    print("\n4. 模拟多日使用效果")
    print("-" * 30)
    print("核心功能演示完成！")
    print("• 情绪日记记录与AI回应")
    print("• 个性化话题推荐")
    print("• 情绪趋势分析")
    print("\n模拟数据已生成，实际项目中会接入大语言模型API")
    print("=" * 50)


if __name__ == "__main__":
    main()