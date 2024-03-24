<p>请求查询二级代理商信息</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTTRADEINFO/">OnRspQrySecAgentTradeInfo</a></p>
<span class="anchor" id="c77368b2-35c5-4f26-8d9f-37b4687f34cb"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="7e404c9a-ef50-40ee-9ba2-7b2d49e75ff4"></span>
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
<span class="anchor" id="e5f5af63-8c50-4172-9229-d3a541a230fa"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="25539f32-94cd-48f1-8ac8-67d1d82534bd"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f1698245-198b-4614-adf2-76eb60a260da"></span>
## 5.FAQ
<p>无</p>
