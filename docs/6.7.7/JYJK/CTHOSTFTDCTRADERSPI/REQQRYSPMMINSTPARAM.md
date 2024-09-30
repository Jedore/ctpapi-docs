<p>请求SPMM合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMINSTPARAM/">OnRspQrySPMMInstParam</a></p>
<span class="anchor" id="9be27501-a5da-49d6-9723-ccf71582d588"></span>
## 1.函数原型
<p>virtual int ReqQrySPMMInstParam(CThostFtdcQrySPMMInstParamField *pQrySPMMInstParam, int nRequestID) = 0;</p>
<span class="anchor" id="3e7e553e-42a1-4ffd-851c-37301b03a8e6"></span>
## 2.参数
<p>pQrySPMMInstParam：SPMM合约参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d17fd070-3d43-487b-ac2a-7987478fa77b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="95631e05-ddd8-4aca-82d8-cefb279469f0"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0171b468-dca1-4f11-a5cc-4f3985d40b99"></span>
## 5.FAQ
<p>无</p>
