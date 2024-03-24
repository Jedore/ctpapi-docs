<p>请求查询经纪公司交易参数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGPARAMS/">ReqQryBrokerTradingParams</a>后，该方法被调用</p>
<span class="anchor" id="f93c7963-26aa-4f50-ab02-5613e6e69d8e"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="752b705c-2bf1-4edc-95fa-1c94c02532c7"></span>
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
<span class="anchor" id="fa222ec4-ed74-4594-a88a-84e16fc2d661"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="97007cdc-2286-40aa-a5e0-5b76e689f4a5"></span>
## 4.FAQ
<p>无</p>
