<p>请求组合优惠比例响应，当执行ReqQryCombPromotionParam后，该方法被调用。</p>
<span class="anchor" id="d84de3cc-10e7-40c8-a883-06cf9b4ced52"></span>
## 1.函数原型
<p>virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e6e23aca-dbc9-41ae-9b09-b3ae5578f8cb"></span>
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
<span class="anchor" id="bf87bcab-468c-4a8d-9d45-1717b0fbbc10"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2b943acd-da4e-45e8-bec7-430746404dfa"></span>
## 4.FAQ
<p>无</p>
