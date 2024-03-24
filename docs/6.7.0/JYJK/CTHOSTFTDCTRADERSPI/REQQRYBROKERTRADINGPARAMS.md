<p>请求查询经纪公司交易参数</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p><strong><font color="#FF0000">只能用投资者账号登录才能查到，不能用操作员登录去查</font></strong></p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYBROKERTRADINGPARAMS/">OnRspQryBrokerTradingParams</a></p>
<span class="anchor" id="7c9c7055-3a03-4e51-8821-75bb1dafd346"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;</p>
<span class="anchor" id="3371a269-2b21-4ce3-9422-487ed63a6455"></span>
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
<span class="anchor" id="29af5053-f081-486e-84f7-016703c8f1d7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="02d1de31-eebd-4412-9321-757242b6315f"></span>
## 4.调用示例
<pre><code>CThostFtdcQryBrokerTradingParamsField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryBrokerTradingParams(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="11634269-fdfe-469d-8e71-71f7163b3dc1"></span>
## 5.FAQ
<p>无</p>
