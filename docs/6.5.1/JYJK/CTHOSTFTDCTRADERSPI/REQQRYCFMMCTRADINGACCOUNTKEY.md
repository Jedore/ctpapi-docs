<p>请求查询保证金监管系统经纪公司资金账户密钥，<strong>此接口已弃用</strong>，请使用ReqQueryCFMMCTradingAccountToken查询。</p>
<p>响应: OnRspQryCFMMCTradingAccountKey</p>
<span class="anchor" id="f4d762a7-5560-44b4-b85c-9c92c6f99d82"></span>
## 1.函数原型
<p>virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) = 0;</p>
<span class="anchor" id="ddf33e64-1305-4fb4-8167-13727d715ef9"></span>
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
<span class="anchor" id="2e9ab2f9-c368-45ba-b727-a415709d6ef9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="577e40c2-12e2-4d49-892c-a6d84e70cdb3"></span>
## 4.调用示例
<pre><code>CThostFtdcQryCFMMCTradingAccountKeyField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryCFMMCTradingAccountKey(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="64b36a12-c195-4813-85c8-bdc981436591"></span>
## 5.FAQ
<p>无</p>
