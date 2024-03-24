<p>请求查询交易通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADINGNOTICE/">OnRspQryTradingNotice</a></p>
<span class="anchor" id="e4b8d6ca-cf30-4f33-a975-9454c2e06505"></span>
## 1.函数原型
<p>virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;</p>
<span class="anchor" id="d075867a-7b55-45ae-8be3-2b36873e839a"></span>
## 2.参数
<p>pQryTradingNotice：查询交易事件通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="fd14da1c-d457-4e23-a5c6-b580495f4302"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="51758544-1978-41ab-bd05-029733a0e5ff"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="395eb8b4-1215-4b56-9b71-a887e1245547"></span>
## 5.FAQ
<p>无</p>
