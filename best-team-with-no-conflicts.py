class Solution {
public:
  int bestTeamScore(vector<int>& scores, vector<int>& ages) {
      vector<vector<int>>v;
      int n = scores.size();
      int mx = 0;
      for(int i=0;i<n;i++)
      {
          v.push_back({scores[i],ages[i]});
          mx = max(mx,ages[i]);
      }
      sort(v.begin(),v.end());     
      vector<vector<int>>dp(n,vector<int>(mx+1,-1));
      return solve(0,0,v,dp);
  }
  int solve(int i, int maxAge,vector<vector<int>> &team,vector<vector<int>>& dp)
  {
      if(i == team.size()) return 0;
      int &ret = dp[i][maxAge];
      if(ret != -1) return ret;
      // possible to take, so consider both options
      if(team[i][1]>=maxAge)
      {
          ret = max(ret,team[i][0]+solve(i+1,team[i][1],team,dp)); // take
          ret = max(ret,solve(i+1,maxAge,team,dp)); // don't take
          return ret;
      }
      // otherwise just don't take
      return ret = solve(i+1,maxAge,team,dp);
  }
};