<p>请求查询经纪公司交易参数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGPARAMS/">ReqQryBrokerTradingParams</a>后，该方法被调用</p>
<span class="anchor" id="0b14e527-b7b6-4f89-a129-daf5f8c59d4d"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8bfb2094-13e3-4b4a-a131-debbb2c5da9f"></span>
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
<span class="anchor" id="da81f969-49df-4693-ac66-d601aa67a3f9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aed765e7-9f4e-4cdd-8da6-0e96bd01751d"></span>
## 4.FAQ
<p>无</p>
