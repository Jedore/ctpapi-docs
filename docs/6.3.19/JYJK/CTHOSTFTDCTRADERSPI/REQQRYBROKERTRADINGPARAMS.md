<p>请求查询经纪公司交易参数</p>
<p>响应: OnRspQryBrokerTradingParams</p>
<span class="anchor" id="0f48696a-14b3-4652-9f86-551a91b6c512"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;</p>
<span class="anchor" id="873c47b9-2352-4bc4-9ec3-9b6179e9517b"></span>
## 2.参数
<p>pQryBrokerTradingParams：查询经纪公司交易参数</p>
<pre><code>struct CThostFtdcQryBrokerTradingParamsField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ebc0ae52-2790-49a9-bfde-368efc333bf8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b9b35bfa-f728-42dd-8690-f167d5ffd122"></span>
## 4.调用示例
<pre><code>CThostFtdcQryBrokerTradingParamsField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryBrokerTradingParams(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="a5a34f2a-6e81-429b-9b40-1cc7a2465cff"></span>
## 5.FAQ
<p>无</p>
