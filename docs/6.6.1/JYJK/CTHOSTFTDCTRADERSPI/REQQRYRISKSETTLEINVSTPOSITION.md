<p>投资者风险结算持仓查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRISKSETTLEINVSTPOSITION/">OnRspQryRiskSettleInvstPosition</a></p>
<p>详见  <a href="../../../6.6.1P1BBGXSM/">6.6.1P1版本更新说明</a></p>
<span class="anchor" id="a0d06eff-a201-4b5a-a556-8944cd13ec59"></span>
## 1.函数原型
<p>virtual int ReqQryRiskSettleInvstPosition(CThostFtdcQryRiskSettleInvstPositionField *pQryRiskSettleInvstPosition, int nRequestID) = 0;</p>
<span class="anchor" id="ad268b33-d5ed-4831-9170-bb435ce086b6"></span>
## 2.参数
<p>pQryRiskSettleInvstPosition：投资者风险结算持仓查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="50e3266a-b713-47eb-b0be-a8a834199c8a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="16143d95-8926-4c39-8c6c-cd544bdd3116"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="d6dd2a75-2150-4c61-a25a-6927d177ed39"></span>
## 5.FAQ
<p>无</p>
