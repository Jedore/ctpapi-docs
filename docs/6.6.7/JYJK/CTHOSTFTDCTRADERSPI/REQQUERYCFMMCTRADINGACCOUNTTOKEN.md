<p>请求查询监控中心用户令牌，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQUERYCFMMCTRADINGACCOUNTTOKEN/">OnRspQueryCFMMCTradingAccountToken</a>、<a href="../../CTHOSTFTDCTRADERAPI/ONRTNCFMMCTRADINGACCOUNTTOKEN/">OnRtnCFMMCTradingAccountToken</a>。</p>
<span class="anchor" id="706bfdf1-8580-49f8-a52b-a2976accee9f"></span>
## 1.函数原型
<p>virtual int ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) = 0;</p>
<span class="anchor" id="ede1a98b-cc5b-454b-ad6a-8c31c1c37d22"></span>
## 2.参数
<p>pQueryCFMMCTradingAccountToken：查询监控中心用户令牌</p>
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
<span class="anchor" id="566e7389-4936-45f9-9f54-fa075c24bf83"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3b0f7691-4f7a-471a-9a99-51d043d420b6"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a4ff8cfc-9908-4c71-a84e-585d10d0e253"></span>
## 5.FAQ
<p>无</p>
