<p>请求查询二级代理商信息</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTTRADEINFO/">OnRspQrySecAgentTradeInfo</a></p>
<span class="anchor" id="b010856f-ce3d-439d-a290-60c06a5a6b63"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="6ff09465-61a8-4b06-9725-98c046b2161d"></span>
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
<span class="anchor" id="2a4bb346-9ae3-4c82-acb0-b6a350cc071d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3d262bba-7579-4ede-8e42-b780f8923cd1"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4fa0d9bd-ade9-463b-8d5a-25fe1c1acff3"></span>
## 5.FAQ
<p>无</p>
