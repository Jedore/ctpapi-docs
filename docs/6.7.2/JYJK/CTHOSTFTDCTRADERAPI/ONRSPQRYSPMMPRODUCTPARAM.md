<p>请求SPMM产品参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPMMPRODUCTPARAM/">ReqQrySPMMProductParam</a>后，该方法被调用。</p>
<span class="anchor" id="0c3a5312-9e62-4306-bf89-7621c9c656ed"></span>
## 1.函数原型
<p>virtual void OnRspQrySPMMProductParam(CThostFtdcSPMMProductParamField *pSPMMProductParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="71e40831-95e2-42d4-a98d-7355dc1a2be5"></span>
## 2.参数
<p>pSPMMProductParam：SPMM产品参数</p>
<pre><code>struct CThostFtdcSPMMProductParamField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品代码
    TThostFtdcSPMMProductIDType ProductID;
    ///商品组代码
    TThostFtdcSPMMProductIDType CommodityID;
    ///商品群代码
    TThostFtdcSPMMProductIDType CommodityGroupID;
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
<span class="anchor" id="3972428f-ec18-4357-b6f3-faa063dcad1c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e88dca8d-5331-439f-a313-5a660e583fb4"></span>
## 4.FAQ
<p>无</p>
