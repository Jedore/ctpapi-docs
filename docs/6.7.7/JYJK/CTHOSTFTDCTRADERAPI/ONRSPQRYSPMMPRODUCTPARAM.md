<p>请求SPMM产品参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPMMPRODUCTPARAM/">ReqQrySPMMProductParam</a>后，该方法被调用。</p>
<span class="anchor" id="7a75846f-3a6a-4dc7-b423-6a2203594f33"></span>
## 1.函数原型
<p>virtual void OnRspQrySPMMProductParam(CThostFtdcSPMMProductParamField *pSPMMProductParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4b4ae593-3fe4-4029-b15f-691659935aac"></span>
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
<span class="anchor" id="36b82e2e-c1b9-468b-9e19-e5806453bd09"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5b5731c6-2814-426d-99ee-fa108ca957e5"></span>
## 4.FAQ
<p>无</p>
