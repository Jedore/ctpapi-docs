<p>请求查询组播合约响应</p>
<span class="anchor" id="472782ac-726a-4a16-ac88-d15dbb575c67"></span>
## 1.函数原型
<p>virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="09888cdd-2c82-4e51-9e69-bf3b1ff311cf"></span>
## 2.参数
<p>MulticastInstrument：组播合约信息</p>
<pre><code>    struct CThostFtdcMulticastInstrumentField
    {
        ///主题号
        TThostFtdcInstallIDType TopicID;
        ///合约代码
        TThostFtdcInstrumentIDType  InstrumentID;
        ///合约编号
        TThostFtdcInstallIDType InstrumentNo;
        ///基准价
        TThostFtdcPriceType CodePrice;
        ///合约数量乘数
        TThostFtdcVolumeMultipleType    VolumeMultiple;
        ///最小变动价位
        TThostFtdcPriceType PriceTick;
    };
</code></pre>
<p>pRspInfo：错误响应</p>
<pre><code>    struct CThostFtdcRspInfoField
    {
        ///错误代码
        TThostFtdcErrorIDType ErrorID;
        ///错误信息
        TThostFtdcErrorMsgType ErrorMsg;
    };
</code></pre>
<span class="anchor" id="77bfc5b6-f3b8-489b-b091-9d8e7f4f558d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="35f95ba4-bac4-4ea1-b286-ee1f443e393e"></span>
## 4.FAQ
<p>无</p>
