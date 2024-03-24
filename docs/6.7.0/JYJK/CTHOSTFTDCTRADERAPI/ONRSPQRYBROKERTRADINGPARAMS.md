<p>请求查询经纪公司交易参数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGPARAMS/">ReqQryBrokerTradingParams</a>后，该方法被调用</p>
<span class="anchor" id="b957d81c-6fe3-4f3a-b3eb-82e7330e7717"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="92d262f6-a431-4c92-b300-dc5c4c930b06"></span>
## 2.参数
<p>pBrokerTradingParams：经纪公司交易参数</p>
<pre><code>struct CThostFtdcBrokerTradingParamsField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///保证金价格类型
    TThostFtdcMarginPriceTypeType MarginPriceType;
    ///盈亏算法
    TThostFtdcAlgorithmType Algorithm;
    ///可用是否包含平仓盈利
    TThostFtdcIncludeCloseProfitType AvailIncludeCloseProfit;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///期权权利金价格类型
    TThostFtdcOptionRoyaltyPriceTypeType OptionRoyaltyPriceType;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
};
</code></pre>
<p>Algorithm：根随期货公司柜台的设置。</p>
<p>OptionRoyaltyPriceType：该算法针对期权保证金算法，而非权利金算法；只限今开仓。</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="dcf864a9-2206-466d-bdf2-40f18daa53e7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="65d15c01-24ab-450e-ab7b-b79ef367e099"></span>
## 4.FAQ
<p>无</p>
