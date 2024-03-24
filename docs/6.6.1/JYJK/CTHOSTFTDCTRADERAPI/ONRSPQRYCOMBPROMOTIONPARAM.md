<p>请求组合优惠比例响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBPROMOTIONPARAM/">ReqQryCombPromotionParam</a>后，该方法被调用。</p>
<span class="anchor" id="027cb69a-5b47-4e6a-85ed-a4e82fb107b8"></span>
## 1.函数原型
<p>virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="aca9fb61-18f0-4373-a213-432e7abf7fae"></span>
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
<span class="anchor" id="ce193760-e4fd-4e54-821a-4f06c447a7a8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="716de06d-0bbf-43c0-9b76-42af2d3639b5"></span>
## 4.FAQ
<p>无</p>
