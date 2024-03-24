<p>请求查询保证金监管系统经纪公司资金账户密钥，<strong>此接口已弃用</strong>，请使用ReqQueryCFMMCTradingAccountToken查询。</p>
<p>响应: OnRspQryCFMMCTradingAccountKey</p>
<span class="anchor" id="054bd248-a488-4019-96ab-4e53d62ff91c"></span>
## 1.函数原型
<p>virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) = 0;</p>
<span class="anchor" id="54a9c56f-9ab8-4a09-b92d-cdffd507f701"></span>
## 2.参数
<p>pQryCFMMCTradingAccountKey：请求查询保证金监管系统经纪公司资金账户密钥</p>
<pre><code>struct CThostFtdcQryCFMMCTradingAccountKeyField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="38bc5182-40e9-444a-a68d-a704eea17b3c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9f1c70f6-108a-4487-92e6-d304370b1d0d"></span>
## 4.调用示例
<pre><code>CThostFtdcQryCFMMCTradingAccountKeyField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryCFMMCTradingAccountKey(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="700cb780-0d46-4ba5-a6c4-b29d9ba7c3cb"></span>
## 5.FAQ
<p>无</p>
