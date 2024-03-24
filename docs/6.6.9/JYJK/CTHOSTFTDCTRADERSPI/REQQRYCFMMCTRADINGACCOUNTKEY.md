<p>请求查询保证金监管系统经纪公司资金账户密钥，<strong>此接口已弃用</strong>，请使用<a href="../REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>查询。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCFMMCTRADINGACCOUNTKEY/">OnRspQryCFMMCTradingAccountKey</a></p>
<span class="anchor" id="23446c62-362a-45e6-96d0-9acdc5dbea9e"></span>
## 1.函数原型
<p>virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) = 0;</p>
<span class="anchor" id="ce31297f-8404-48bf-b7f4-e3c3ac6f4086"></span>
## 2.参数
<p>pQryCFMMCTradingAccountKey：请求查询保证金监管系统经纪公司资金账户密钥</p>
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
</table>
<blockquote>
<p>接口弃用</p>
</blockquote>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="14dbe727-a140-43b7-bb4a-fe08636a43a5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ab6be9d1-23b8-4386-81f3-8fcc02e599bb"></span>
## 4.调用示例
<pre><code>CThostFtdcQryCFMMCTradingAccountKeyField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryCFMMCTradingAccountKey(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="5bcbccb7-f36b-41fb-83dd-2f4c92561bb3"></span>
## 5.FAQ
<p>无</p>
