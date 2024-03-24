<p>请求查询保证金监管系统经纪公司资金账户密钥，<strong>此接口已弃用</strong>，请使用<a href="../REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>查询。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCFMMCTRADINGACCOUNTKEY/">OnRspQryCFMMCTradingAccountKey</a></p>
<span class="anchor" id="97bd6168-561e-47fa-b2f8-0f6ad111eba7"></span>
## 1.函数原型
<p>virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) = 0;</p>
<span class="anchor" id="b85ae71d-00cb-4236-9cb7-42c7f0a648af"></span>
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
<span class="anchor" id="be350dd5-4ae0-4ff0-9905-3ae5a293f94f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7935f1bb-aab0-47e9-b0b3-0ab6af38216e"></span>
## 4.调用示例
<pre><code>CThostFtdcQryCFMMCTradingAccountKeyField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryCFMMCTradingAccountKey(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="8d7d7bcc-afc3-4450-9992-58cf5e014907"></span>
## 5.FAQ
<p>无</p>
