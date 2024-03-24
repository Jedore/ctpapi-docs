<p>请求查询二级代理商信息</p>
<p>响应: OnRspQrySecAgentTradeInfo</p>
<span class="anchor" id="74c386a8-7cfc-42b6-80d9-9d0df7620317"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="18cb2d9e-e8d1-4f12-b1ca-0e2d6cc0b515"></span>
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
<span class="anchor" id="9185aebd-1ef9-49ea-a349-87bbb6fd1106"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ce763add-e495-4bb1-8562-a3c9bbe5246e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c86f9f26-0e3c-48cb-b3c7-ab95d28246e7"></span>
## 5.FAQ
<p>无</p>
