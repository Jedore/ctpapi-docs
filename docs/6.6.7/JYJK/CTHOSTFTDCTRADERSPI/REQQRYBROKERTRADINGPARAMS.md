<p>请求查询经纪公司交易参数</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p><strong><font color="#FF0000">只能用投资者账号登录才能查到，不能用操作员登录去查</font></strong></p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYBROKERTRADINGPARAMS/">OnRspQryBrokerTradingParams</a></p>
<span class="anchor" id="b28bfb44-8d1e-409d-8762-20962713d004"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;</p>
<span class="anchor" id="d47ad858-4f20-466f-8700-4df85ae2547d"></span>
## 2.参数
<p>pQryBrokerTradingParams：查询经纪公司交易参数</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="67cc6386-d93b-4104-a2d7-d7d3b80a94b0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="26194c13-c0f7-439e-af91-85a4d883fcaa"></span>
## 4.调用示例
<pre><code>CThostFtdcQryBrokerTradingParamsField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryBrokerTradingParams(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="9a377d97-ba8d-44d7-8bb1-6e0e00ae760b"></span>
## 5.FAQ
<p>无</p>
