<p>请求查询二级代理商信息</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTTRADEINFO/">OnRspQrySecAgentTradeInfo</a></p>
<span class="anchor" id="410791c8-d7ae-4890-87c0-0fdb970459c1"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="3b13f8f1-2c06-41a3-b1db-fce32b951d97"></span>
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
<span class="anchor" id="fdac7e8f-6523-4cfa-958f-8f85d04a32eb"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d717cfb2-6f60-4017-90f0-ffa0593789e1"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="258383b8-ca98-4b4b-bc6f-7fd2eb38f416"></span>
## 5.FAQ
<p>无</p>
