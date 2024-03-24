<p>请求组合优惠比例响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBPROMOTIONPARAM/">ReqQryCombPromotionParam</a>后，该方法被调用。</p>
<span class="anchor" id="ec716593-59e4-4dd6-bc0e-5fde7dce820a"></span>
## 1.函数原型
<p>virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="60593913-32fc-49d5-9f17-85822861e01b"></span>
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
<span class="anchor" id="55dc1dce-90bb-45c2-a19c-23a3d7c56e98"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="88353ea3-e2c6-4a76-b5cf-6ff8a639d9c6"></span>
## 4.FAQ
<p>无</p>
