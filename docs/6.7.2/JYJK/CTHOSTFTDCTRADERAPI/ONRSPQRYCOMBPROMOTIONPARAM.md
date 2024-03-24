<p>请求组合优惠比例响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBPROMOTIONPARAM/">ReqQryCombPromotionParam</a>后，该方法被调用。</p>
<span class="anchor" id="0c142685-028b-437a-8714-0083f1eb12bd"></span>
## 1.函数原型
<p>virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="abae5ef6-87fc-4d34-9156-c85489cba488"></span>
## 2.参数
<p>pCombPromotionParam：组合优惠比例</p>
<pre><code>struct CThostFtdcCombPromotionParamField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///投机套保标志
    TThostFtdcCombHedgeFlagType CombHedgeFlag;
    ///期权组合保证金比例
    TThostFtdcDiscountRatioType Xparameter;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="0db61617-c232-4aa0-9916-94df158acec0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a01bee63-5b2e-48cf-ba63-e549fb834c72"></span>
## 4.FAQ
<p>无</p>
