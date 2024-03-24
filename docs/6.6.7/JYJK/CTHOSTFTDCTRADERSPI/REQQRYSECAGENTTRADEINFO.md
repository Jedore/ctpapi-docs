<p>请求查询二级代理商信息</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTTRADEINFO/">OnRspQrySecAgentTradeInfo</a></p>
<span class="anchor" id="3a699d75-994f-4cbe-a315-f1c0ad3a0b1c"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="fe74c332-843d-478a-a51e-14257126fd46"></span>
## 2.参数
<p>pQrySecAgentTradeInfo：查询二级代理商信息</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">BrokerSecAgentID</td>
<td style="TEXT-ALIGN: left;">境外中介机构资金帐号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="212530ad-07c3-42e6-914c-a86927bb7784"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="102601a5-9d28-466a-bbf9-8799a8101058"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8f468828-d30d-4e35-bb35-feae2eaf3751"></span>
## 5.FAQ
<p>无</p>
