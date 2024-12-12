<p>请求组合优惠比例响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBPROMOTIONPARAM/">ReqQryCombPromotionParam</a>后，该方法被调用。</p>
<span class="anchor" id="ba0f1fcd-d565-404f-abff-a3365376f6d7"></span>
## 1.函数原型
<p>virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4cfd9f07-0fee-4b09-b074-de083c59874f"></span>
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
<span class="anchor" id="9656d581-0165-42ee-9851-f1d2708cbd4c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1600faa4-d368-4cfc-b059-86d6853062c7"></span>
## 4.FAQ
<p>无</p>
